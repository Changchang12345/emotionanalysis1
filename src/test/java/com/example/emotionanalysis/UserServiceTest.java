package com.example.emotionanalysis;

import com.example.emotionanalysis.entity.EmotionReport;
import com.example.emotionanalysis.entity.User;
import com.example.emotionanalysis.repository.ReportRepository;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;


import java.io.IOException;

import lombok.extern.slf4j.Slf4j;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import com.example.emotionanalysis.service.*;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.annotation.Rollback;
import org.springframework.test.context.junit4.SpringRunner;

import javax.transaction.Transactional;

//@RunWith(SpringRunner.class)
@SpringBootTest

@Slf4j
public class UserServiceTest {
    @Autowired
    userService userService;

//    @Test
//    public void find(String topic) throws IOException {
//        userService.searchByTopic(topic);
//    }
//
    @Transactional
    @Rollback(value = false)
    @Test
    public void init() {
        User s1 = new User();
        s1.setUserName("花花");
        s1.setUserNumber(2017224398);
        userService.addUser(s1);

    }


}