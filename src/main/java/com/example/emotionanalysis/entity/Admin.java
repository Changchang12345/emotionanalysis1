package com.example.emotionanalysis.entity;

import lombok.Data;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import javax.persistence.*;
import java.time.LocalDateTime;


@Data
@NoArgsConstructor
@Getter
@Setter

@Entity
public class Admin {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer adminID;
    private Integer adminNumber;//工号
    private String adminName;//名字
    private String adminPassword;//密码
    @Column(columnDefinition = "timestamp default current_timestamp",
            insertable = false,updatable = false)
    private LocalDateTime insertTime;

}
