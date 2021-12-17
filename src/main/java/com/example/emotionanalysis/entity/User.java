package com.example.emotionanalysis.entity;

import com.example.emotionanalysis.enums.RoleEnums;
import lombok.Data;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import javax.persistence.*;
import java.time.LocalDateTime;
import java.util.List;

@Data
@NoArgsConstructor
@Getter
@Setter

@Entity
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer userID;
    private Integer userNumber;//工号
    private String userName;//名字
    private String userPassword;//密码
    @Column(columnDefinition = "timestamp default current_timestamp",
            insertable = false,updatable = false)
    private LocalDateTime insertTime;
    private String sex;
    private String address;
    private Integer age;

    @Column(columnDefinition = "TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP",
            insertable = false,
            updatable = false)
    private LocalDateTime updateTime;
    private RoleEnums role;
    @OneToMany(mappedBy = "user")
    private List<EmotionReport> emotionReports;
}
