package com.blooddonation.dao;

import java.util.List;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;
import com.blooddonation.model.Donor;

public class DonorDAO {
    private static SessionFactory factory = new Configuration().configure().buildSessionFactory();

    public void saveDonor(Donor donor) {
        Session session = factory.openSession();
        session.beginTransaction();
        session.save(donor);
        session.getTransaction().commit();
        session.close();
    }

    public List<Donor> getAllDonors() {
        Session session = factory.openSession();
        List<Donor> donors = session.createQuery("from Donor", Donor.class).list();
        session.close();
        return donors;
    }
}
