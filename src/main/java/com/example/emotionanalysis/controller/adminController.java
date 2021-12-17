package com.example.emotionanalysis.controller;


import com.example.emotionanalysis.entity.Admin;
import com.example.emotionanalysis.entity.User;
import com.example.emotionanalysis.entity.EmotionReport;
import com.example.emotionanalysis.service.*;
import com.example.emotionanalysis.vo.ResultVO;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.server.ResponseStatusException;

import javax.servlet.http.HttpServletResponse;
import java.util.Map;

@Slf4j
@RestController
@Validated//jiaoyan
@RequestMapping("/api/PublicOpinionAnalysis/")
public class adminController {
//    @Autowired
//    private adminService adminService;
//    @Autowired
//    private PasswordEncoder encoder;
//    @Autowired
//    private userService userService;
//    @Autowired
//    private emotionReportService reportService;
//    @Autowired
//    private EncryptComponent encryptComponent;
//    //登录界面(管理员)
//    @PostMapping("login")
//    public Map postLogin(@RequestBody Admin admin, HttpServletResponse response){
//        Admin a = adminService.(admin.getAdminNumber());
//        //先查询用户是否存在
//        if(a==null||!encoder.matches(admin.getAdminPassword(), a.getAdminPassword())){
//            log.debug("failed");
//            throw new ResponseStatusException(HttpStatus.UNAUTHORIZED,"用户名密码错误");
//        }
//        else {
//            log.debug("登陆成功");//后需添加token操作
//        }
//        return Map.of("Admin",a);
//    }
//    //登录后跳转界面
//    @PostMapping("admin/modify")
//    public Map afterLogin(@RequestBody Admin admin){
//        return Map.of("登录后界面", "三个功能模块");
//    }
//    //管理员修改密码界面
//    @PostMapping("admin/{aid}/modifyPassword")
//    public Map setPasswordA(@PathVariable int aid,String newPassword){
//        adminService.modifyPassword(newPassword,aid);
//        return Map.of("action", "success");
//    }
//    //管理员维护用户信息
//    @PostMapping("admin/modifyUsers")
//    public Map listUsers(@RequestBody Admin admin){
//        return Map.of("用户列表",userService.listUsers());
//    }
//    //删除用户
//    @GetMapping("admin/modifyUsers/{uid}/deleteUser")
//    public Map deleteUser(@PathVariable int uid){
//        userService.deleteUser(uid);
//        return Map.of("massage","已成功删除！");
//    }
//    //查询用户
//    @GetMapping("admin/modifyUsers/{uid}/searchUser")
//    public Map searchUser(@PathVariable int uid){
//        userService.getUser(uid);
//        return Map.of("用户",userService.getUser(uid));
//    }
//    //管理员维护报告信息
//    @PostMapping("admin/modifyReports")
//    public Map listReports(@RequestBody Admin admin){
//        return Map.of("报告列表",reportService.listReports());
//    }
//    //删除报告
//    @GetMapping("admin/modifyReports/{eid}/deleteReport")
//    public Map deleteReport(@PathVariable int rid){
//        reportService.deleteReport(rid);
//        return Map.of("massage","已成功删除！");
//    }
//    //查询报告
//    @GetMapping("admin/modifyReports/{rid}/searchReport")
//    public Map searchReport(@PathVariable int rid){
//        return Map.of("报告",reportService.findReportById(rid));
//    }
}
