package com.gqt;

import java.io.Serializable;

public class Voter implements Serializable {
    private String username;
    private String password;
    private boolean voted;

    public Voter(String username, String password) {
        this.username = username;
        this.password = password;
        this.voted = false;
    }

    public Voter(String username, String password, boolean voted) {
        this.username = username;
        this.password = password;
        this.voted = voted;
    }

    public String getUsername() {
        return username;
    }

    public String getPassword() {
        return password;
    }

    public boolean hasVoted() {
        return voted;
    }

    public void setVoted(boolean voted) {
        this.voted = voted;
    }

    public String toText() {
        return username + ":" + password + ":" + voted;
    }

    public static Voter fromText(String line) {
        String[] parts = line.split(":");
        return new Voter(parts[0], parts[1], Boolean.parseBoolean(parts[2]));
    }
}
