package com.rorrim.mang.smartmirror;

import java.io.IOException;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.ProtocolException;
import java.net.URL;

public class HttpMgrThread extends Thread{

    private final int TIME_OUT = 20;
    private final String GET_METHOD = "GET";
    private String addr;
    private HttpURLConnection conn;

    public HttpMgrThread(String addr){
        this.addr = addr;
    }

    @Override
    public void run(){
        reqHttp();
    }

    private void reqHttp(){
        try {
            URL url = new URL(addr);
            conn = (HttpURLConnection) url.openConnection();
            this.setRequest();
            conn.connect();

        }catch(IOException e){
            e.printStackTrace();
        }
    }

    private void setRequest(){
        // Connect Time out
        conn.setConnectTimeout(TIME_OUT * 1000);

        // Read Time out
        conn.setReadTimeout(TIME_OUT * 1000);

        // Choose Method
        try {
            conn.setRequestMethod(GET_METHOD);
        } catch (ProtocolException e) {
            e.printStackTrace();
        }
    }


}
