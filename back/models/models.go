package models

import "time"

// Post struct
type Post struct {
	ID       int16
	Title    string
	Author   string
	Text     string
	PostTime time.Time
}
