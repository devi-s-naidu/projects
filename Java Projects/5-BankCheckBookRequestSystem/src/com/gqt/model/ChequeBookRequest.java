package com.gqt.model;

import java.util.Date;

public class ChequeBookRequest {
    private String requestId;
    private String accountNumber;
    private Date requestDate;
    private String status; 
    private int numberOfLeaves; 
    
    public ChequeBookRequest(String requestId, String accountNumber, Date requestDate, 
                            String status, int numberOfLeaves) {
        this.requestId = requestId;
        this.accountNumber = accountNumber;
        this.requestDate = requestDate;
        this.status = status;
        this.numberOfLeaves = numberOfLeaves;
    }

    public String getRequestId() {
        return requestId;
    }

    public String getAccountNumber() {
        return accountNumber;
    }

    public Date getRequestDate() {
        return requestDate;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public int getNumberOfLeaves() {
        return numberOfLeaves;
    }
}