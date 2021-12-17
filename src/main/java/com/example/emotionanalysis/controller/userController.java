package com.example.emotionanalysis.controller;


import com.example.emotionanalysis.entity.Admin;
import com.example.emotionanalysis.entity.User;
import com.example.emotionanalysis.entity.EmotionReport;
import com.example.emotionanalysis.service.*;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.server.ResponseStatusException;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

import javax.jms.Topic;
import java.util.Map;

@Slf4j
@RestController
@Validated//jiaoyan
@RequestMapping("/api/PublicOpinionAnalysis/")
public class userController {
//    @Autowired
//    private adminService adminService;
//    @Autowired
//    private PasswordEncoder encoder;
//    @Autowired
//    private userService userService;
//    @Autowired
//    private emotionReportService reportService;
//    //登录界面(用户)
//    @PostMapping("login")
//    public Map postLogin(@RequestBody User user){
//        User u = userService.findUserByName(user.getUserName());
//        //先查询用户是否存在
//        if(u==null||!encoder.matches(user.getUserPassword(), u.getUserPassword())){
//            log.debug("failed");
//            throw new ResponseStatusException(HttpStatus.UNAUTHORIZED,"用户名或密码错误");
//        }
//        else {
//            log.debug("登陆成功");//后需添加token操作
//        }
//        return Map.of("User",u);
//    }
//    //注册界面
//    @PostMapping("user/postLogin")
//    public Map log(@RequestBody User user){
//       return userService.logUser(user.getUserName(), user.getUserPassword());
//
//    }
//    //查询舆情分析报告
//    @GetMapping("/user/{topic}")
//    public Map getReport(@PathVariable String topic) throws IOException {
//
//        return Map.of("生成报告",userService.searchByTopic(topic));
//    }
//    //搜索界面
//    @PostMapping("user/search")
//    public Map search(@RequestBody User user) throws IOException {
//
//        return Map.of("登录后跳转界面","搜索框");
//
//    }
//    //个人中心界面
//    @GetMapping("user/{uid}")
//    public Map info(@RequestBody User u){
//        return Map.of("user",u);
//    }
//    //save个人信息
//    @PostMapping("user/{uid}")
//    public Map editInfo(@PathVariable Integer uid, String name,String sex,Integer age,String address){
//        userService.getUser(uid).setUserName(name);
//        userService.getUser(uid).setAddress(address);
//        userService.getUser(uid).setAge(age);
//        userService.getUser(uid).setSex(sex);
//        return Map.of("Newuser",userService.getUser(uid));
//    }
//    @PostMapping("user/{uid}modifyPassword")
//    public Map modifyPS(@PathVariable Integer uid,String newPassword){
//        userService.modifyPassword(newPassword, userService.getUser(uid).getUserName());
//        return Map.of("Newuser",userService.getUser(uid));
//    }
}
