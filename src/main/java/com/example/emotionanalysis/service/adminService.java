package com.example.emotionanalysis.service;

import com.example.emotionanalysis.entity.*;
import com.example.emotionanalysis.repository.*;
import lombok.Getter;
import lombok.Setter;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.annotation.CreatedBy;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;

import javax.transaction.Transactional;
import java.util.ArrayList;
import java.util.Base64;
import java.util.List;
import java.util.Map;

@Getter
@Setter
@Service
@Transactional
public class adminService {
//    @Autowired
//    AdminRepository adminRepository;
//    @Autowired
//    PasswordEncoder encoder;
//    @Autowired
//    UserRepository userRepository;
//    @Autowired
//    ReportRepository reportRepository;
//    //创建管理员
//    private Map<Integer,Admin> adminMap = createAdmin();
//    private Map createAdmin(){
//        Admin a = new Admin();
//        a.setAdminNumber(2021001);
//        a.setAdminPassword("$2a$10$WJcH4PHTOrHEeL/0.v0NauYALumYPfFDJxd6bl4JhpgoXU5GR1v3u");
//        return Map.of(a.getAdminNumber(),a);
//    }
//    public Admin getAdmin(int aNumber){
//        return adminMap.get(aNumber);
//    }
//
//    //删除管理员
//    public void deleteAdmin(int adminId){
//        adminRepository.deleteAdminById(adminId);
//    }
//
//    //admin修改密码
//    public void modifyPassword(String Password,Integer aid){
//        String newPassword = encoder.encode(Password);
//        adminRepository.findById(aid).orElse(null).setAdminPassword(Password);
//    }
//    //根据number寻找管理员
//    public Admin findByNum(Integer number){
//        return adminRepository.findByAdminNumber(number);
//    }


}
