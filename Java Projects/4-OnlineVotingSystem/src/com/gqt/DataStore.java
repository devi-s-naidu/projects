package com.gqt;

import java.io.*;
import java.util.*;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class DataStore {
    public static HashMap<String, Voter> voters = new HashMap<>();
    public static HashMap<String, Candidate> candidates = new HashMap<>();

    private static final String VOTER_FILE = "voters.txt";
    private static final String CANDIDATE_FILE = "candidates.txt";

    public static void loadData() {
        try (BufferedReader br = new BufferedReader(new FileReader(VOTER_FILE))) {
            String line;
            while ((line = br.readLine()) != null) {
                if (line.contains("(Saved on:")) {
                    line = line.split("\\(Saved on:")[0].trim();
                }
                Voter v = Voter.fromText(line);
                voters.put(v.getUsername(), v);
            }
        } catch (IOException e) {
            System.out.println("No voters.txt found, starting fresh.");
        }

        try (BufferedReader br = new BufferedReader(new FileReader(CANDIDATE_FILE))) {
            String line;
            while ((line = br.readLine()) != null) {
                if (line.contains("(Saved on:")) {
                    line = line.split("\\(Saved on:")[0].trim();
                }
                Candidate c = Candidate.fromText(line);
                candidates.put(c.getName(), c);
            }
        } catch (IOException e) {
            System.out.println("No candidates.txt found, starting fresh.");
        }
    }

    public static void saveData() {
        DateTimeFormatter dtf = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
        String timestamp = dtf.format(LocalDateTime.now());

        try (PrintWriter pw = new PrintWriter(new FileWriter(VOTER_FILE))) {
            for (Voter v : voters.values()) {
                pw.println(v.toText() + " (Saved on: " + timestamp + ")");
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        try (PrintWriter pw = new PrintWriter(new FileWriter(CANDIDATE_FILE))) {
            for (Candidate c : candidates.values()) {
                pw.println(c.toText() + " (Saved on: " + timestamp + ")");
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
