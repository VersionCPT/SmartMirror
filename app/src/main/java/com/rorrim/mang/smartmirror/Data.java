package com.rorrim.mang.smartmirror;

public class Data {
    private String status;
    private String result;

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public String getResult() {
        return result;
    }

    public void setResult(String result) {
        this.result = result;
    }

    @Override
    public String toString() {
        return "Data [status=" + status + ", result=" + result;
    }

}
