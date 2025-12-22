package com.gqt.model;

import javax.persistence.*;

@Entity
@Table(name = "review_questions")
public class Question {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int id;
    private String question;
	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	public String getQuestion() {
		return question;
	}
	public void setQuestion(String question) {
		this.question = question;
	}
    
}

