package com.example.insig_enc;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.animation.Animation;
import android.view.animation.AnimationUtils;
import android.widget.ImageView;

public class MainActivity extends AppCompatActivity {
    private ImageView img;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        img=(ImageView)findViewById(R.id.image1);
        Animation vecl= (Animation) AnimationUtils.loadAnimation(MainActivity.this,R.anim.mytransition);
        img.startAnimation(vecl);
        final Intent in=new Intent(MainActivity.this,INSIGNIA_ENCORP.class);

        Thread timer =new Thread(){
            public void run(){
                try {
                    sleep(5000);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                finally {
                    startActivity(in);
                }

            }
        };
        timer.start();
    }


}

