package com.example.emotionanalysis.service;

import com.example.emotionanalysis.entity.*;
import com.example.emotionanalysis.repository.*;
import lombok.Getter;
import lombok.Setter;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;

import javax.transaction.Transactional;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Base64;
import java.util.List;
import java.util.Map;

@Getter
@Setter
@Transactional
@Service
public class userService {
    @Autowired
    PasswordEncoder encoder;
    @Autowired
    UserRepository userRepository;
    @Autowired
    ReportRepository reportRepository;
    //用户注册
    public Map logUser(String userName,String userPassword){
        User u = new User();
        if(userRepository.findByUserName(userName)==null){
            u.setUserName(userName);}
        else{
            System.out.println("用户名已存在");
        }
        u.setUserPassword(userPassword);
        addUser(u);
        return Map.of(u.getUserName(), u);
    }
    //当用户注册后添加用户
    public void addUser(User user){
        userRepository.save(user);
    }
    //用户修改密码
    public void modifyPassword(String Password,String userName){
        String newPassword = encoder.encode(Password);
        userRepository.findByUserName(userName).setUserPassword(newPassword);
    }
    //用户搜索话题
    public EmotionReport searchByTopic(String topic) throws IOException {
        Runtime.getRuntime().exec("python \\spider\\topic_spider.py");
        return reportRepository.findByTopic(topic);//嵌入爬取程序python
    }
    //删除用户
    public void deleteUser(int userId) {
        userRepository.deleteUserById(userId);
    }
    //根据用户ID找用户
    public User getUser(int userId){
        return userRepository.findById(userId).orElse(null);
    }
    //根据名字找用户
    public User findUserByName(String name){
        return userRepository.findByUserName(name);
    }
    //例举所有用户
    public List<User> listUsers(){
        return userRepository.listUsers();
    }

}
