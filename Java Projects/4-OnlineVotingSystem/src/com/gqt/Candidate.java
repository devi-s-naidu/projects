package com.gqt;

import java.io.Serializable;

public class Candidate implements Serializable {
    private String name;
    private int votes;

    public Candidate(String name) {
        this.name = name;
        this.votes = 0;
    }

    public Candidate(String name, int votes) {
        this.name = name;
        this.votes = votes;
    }

    public String getName() {
        return name;
    }

    public int getVotes() {
        return votes;
    }

    public void incrementVotes() {
        votes++;
    }

    public String toText() {
        return name + ":" + votes;
    }

    public static Candidate fromText(String line) {
        String[] parts = line.split(":");
        return new Candidate(parts[0], Integer.parseInt(parts[1]));
    }
}
