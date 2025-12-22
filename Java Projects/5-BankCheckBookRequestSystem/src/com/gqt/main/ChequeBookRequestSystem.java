package com.gqt.main;

import javax.swing.SwingUtilities;

import com.gqt.view.LoginFrame;

public class ChequeBookRequestSystem {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                new LoginFrame().setVisible(true);
            }
        });
    }
}
