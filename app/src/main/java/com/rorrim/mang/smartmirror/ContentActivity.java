package com.rorrim.mang.smartmirror;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.widget.TextView;

public class ContentActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.content_main); //해당 아이디에 자신이 만든 레이아웃의 이름을 쓴다
    }

    @Override
    protected void onStart(){
        Intent intent = getIntent();
        setComponent(intent.getStringExtra("status"), intent.getStringExtra("result"));

        super.onStart();
    }

    private void setComponent(String status, String result){
        TextView tv = findViewById(R.id.tv_status);
        tv.setText(status);
        tv = findViewById(R.id.tv_result);
        tv.setText(result);
    }

}
