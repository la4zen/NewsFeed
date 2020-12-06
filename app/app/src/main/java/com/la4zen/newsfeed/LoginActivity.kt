package com.la4zen.newsfeed

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.Button
import android.widget.EditText
import android.widget.Toast
import java.net.URL

class LoginActivity : AppCompatActivity() {

    val url : URL = URL("http://localhost:5000/api")

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_login)
        var loginButton = findViewById<Button>(R.id.loginButton)
        var registerButton = findViewById<Button>(R.id.registerButton)
        var editTextLogin = findViewById<Button>(R.id.editTextLogin)
        var editTextPassword = findViewById<Button>(R.id.editTextPassword)

        loginButton.setOnClickListener(View.OnClickListener {
            var login = editTextLogin.text.toString()
            var password = editTextPassword.text.toString()
            Thread(Runnable {
                
            }).start()
        })
    }
    protected fun result(text : String) {
        runOnUiThread(Runnable {
            Toast.makeText(applicationContext, text, 3).show()
        })
    }
}