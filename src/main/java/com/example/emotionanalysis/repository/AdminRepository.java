package com.example.emotionanalysis.repository;

import com.example.emotionanalysis.entity.User;
import org.springframework.data.jpa.repository.Modifying;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;
import com.example.emotionanalysis.entity.Admin;

import java.util.List;

@Repository
public interface AdminRepository extends BaseRepository<Admin,Integer>{
//    @Query("from Admin a where a.adminName =:name")
//    List<Admin> listA(@Param("name") String name);
//
//    @Modifying
//    @Query("delete from Admin a where a.adminID=:aid")
//    void deleteAdminById(@Param("aid") Integer aid);
//
//    @Query("from Admin a where a.adminName =:name")
//    Admin findByAdminName(@Param("name") String name);
//
//    @Query("from Admin a where a.adminNumber =:number")
//    Admin findByAdminNumber(@Param("number") Integer Anumber);
}
