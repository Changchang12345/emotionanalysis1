package com.example.emotionanalysis.entity;

import lombok.Data;
import lombok.NoArgsConstructor;

import javax.persistence.*;
import java.time.LocalDateTime;

@Data
@NoArgsConstructor
@Entity
public class EmotionReport {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer reportID;
    private Integer topicID;//主题编号
    private String topic;//舆情分析主题
    //性别分布
    //年龄段分布
    //地区分布
    //星座分布
    //词云

    //总结
    @ManyToOne
    private User user;
    @Column(columnDefinition = "timestamp default current_timestamp",
            insertable = false,updatable = false)
    private LocalDateTime insertTime;
}
