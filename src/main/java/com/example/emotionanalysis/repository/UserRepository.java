package com.example.emotionanalysis.repository;

import org.springframework.data.jpa.repository.Modifying;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;
import com.example.emotionanalysis.entity.User;
import com.example.emotionanalysis.entity.EmotionReport;

import java.util.List;

@Repository
public interface UserRepository extends BaseRepository<User,Integer>{

    @Query("from User u where u.userName =:name")
    User findByUserName(@Param("name") String name);

    @Modifying
    @Query("delete from User u where u.userID=:uid")
    void deleteUserById(@Param("uid") Integer uid);

//    @Query("select User.emotionReports from User u where u.userID=:uid")
//    List<EmotionReport> listRE(@Param("uid") Integer uid);

    @Query("from User u")
    List<User> listUsers();
}

