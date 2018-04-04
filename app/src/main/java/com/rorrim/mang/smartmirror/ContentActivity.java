package com.rorrim.mang.smartmirror;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;

public class ContentActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.content_main); //해당 아이디에 자신이 만든 레이아웃의 이름을 쓴다

    }
}
