window.onload = function () {
    var app = new Vue({
        el :"#app",
        data() {
            return {
                editor:false,
                posts:[],
                postEditor:{
                    text:"",
                    title:"",
                    author:""
                },
                change_text:"Добавить пост",
                work:false
            }
        },
        mounted(){

        },
        methods: {
            getPosts : function() {
                axios.post(document.location.origin+":8080/api/v1/getPosts")
                .then(response => {
                    console.log(response)
                    this.posts = response.data.response
                    this.work = true
                }).catch(response => {
                    alert("Нет подключения к серверу")
                })
            },
            postAdd : function () {
                if (this.postEditor.title && this.postEditor.author && this.postEditor.text) {
                    var data = new FormData()
                    data.append("title", this.postEditor.title)
                    data.append("author", this.postEditor.author)
                    data.append("text", this.postEditor.text)
                    axios.post(document.location.origin+":8080/api/v1/addPost", data=data)
                    .then(response => {
                        alert("Пост успешно добавлен!")
                    }).cathc(response => {
                        console.log(response)
                        alert("Нет подключения к серверу")
                    })
                }
            },
            change_editor : function () {
                this.editor = !this.editor
                if (this.editor) {
                    this.change_text = "Посмотреть посты"
                } else {
                    this.change_text = "Добавить пост"
                }
            }
        }
    })
    app.getPosts()
}