package main

import (
	"database/sql"
	"fmt"
	"net/http"

	"./models"
	"github.com/labstack/echo"
	"github.com/labstack/echo/middleware"
	_ "github.com/mattn/go-sqlite3"
)

func main() {
	db, err := sql.Open("sqlite3", "./newsfeed.db")
	if err != nil {
		fmt.Errorf("DB start init error")
	}
	db.Exec(`CREATE TABLE IF NOT EXISTS posts (
		id INTEGER PRIMARY KEY,
		title TEXT,
		author TEXT,
		text TEXT,
		post_time DATETIME DEFAULT CURRENT_TIMESTAMP
	)`)
	db.Close()
	e := echo.New()

	e.Use(middleware.CORSWithConfig(middleware.CORSConfig{
		AllowOrigins: []string{"*"},
		AllowHeaders: []string{echo.HeaderOrigin, echo.HeaderContentType, echo.HeaderAccept},
	}))
	e.Use(middleware.Logger())
	e.Use(middleware.Recover())

	e.POST("/api/v1/getPosts", getPosts)
	e.POST("/api/v1/addPost", addPost)

	e.Logger.Fatal(e.Start(":8080"))
}

func getPosts(c echo.Context) error {
	db, err := sql.Open("sqlite3", "./newsfeed.db")
	if err != nil {
		return c.String(http.StatusInternalServerError, "db connection err")
	}
	defer db.Close()
	posts := []models.Post{}
	rows, err := db.Query("SELECT * FROM posts")
	if err != nil {
		return c.String(http.StatusInternalServerError, "db connection err")
	}
	defer rows.Close()
	for rows.Next() {
		post := models.Post{}
		err = rows.Scan(&post.ID, &post.Title, &post.Author, &post.Text, &post.PostTime)
		if err != nil {
			return c.String(http.StatusInternalServerError, "db get rows failed")
		}
		posts = append(posts, post)
	}
	return c.JSON(http.StatusOK, map[string]interface{}{
		"response": posts,
	})
}

func addPost(c echo.Context) error {
	post := models.Post{
		Title:  c.FormValue("title"),
		Author: c.FormValue("author"),
		Text:   c.FormValue("text"),
	}
	if post.Title == "" || post.Author == "" || post.Text == "" {
		return c.String(http.StatusBadRequest, "title, author and text required")
	}
	db, err := sql.Open("sqlite3", "./newsfeed.db")
	if err != nil {
		return c.String(http.StatusInternalServerError, "db connection err")
	}
	defer db.Close()
	_, err = db.Exec("INSERT INTO posts(title, author, text) VALUES (?, ?, ?)", post.Title, post.Author, post.Text)
	if err != nil {
		return c.String(http.StatusInternalServerError, "db insert values err")
	}
	return c.NoContent(http.StatusAccepted)
}
