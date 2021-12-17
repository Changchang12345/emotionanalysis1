package com.example.emotionanalysis.service;

import com.example.emotionanalysis.entity.*;
import com.example.emotionanalysis.repository.*;
import lombok.Getter;
import lombok.Setter;
import org.springframework.beans.factory.annotation.Autowired;
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
public class emotionReportService {
    @Autowired
    ReportRepository reportRepository;
    //根据报告名称查找发起人
    public List<String> findByTopicName(String tpName){
        return List.of(reportRepository.findByTopic(tpName).getUser().getUserName());
    }
    //保存报告
    public void addReport(EmotionReport report){
        reportRepository.save(report);
    }
    //查询报告
    public EmotionReport findReportById(Integer rid){
        return reportRepository.findById(rid).orElse(null);
    }
    //例举所有报告
    public List<EmotionReport> listReports(){
        return reportRepository.listReports();
    }
    //删除报告
    public void deleteReport(int reportId){
        reportRepository.deleteRE(reportId);
    }
}
