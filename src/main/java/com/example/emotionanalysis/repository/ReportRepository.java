package com.example.emotionanalysis.repository;

import org.springframework.data.jpa.repository.Modifying;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;
import com.example.emotionanalysis.entity.EmotionReport;


import java.util.List;

@Repository
public interface ReportRepository extends BaseRepository<EmotionReport,Integer>{

//    @Query("from EmotionReport e where e.reportID=:rid")
//    EmotionReport findByEid(@Param("rid") Integer rid);

    @Modifying
    @Query("delete from EmotionReport e where e.reportID=:rid")
    void deleteRE(@Param("rid") Integer rid);

    @Query("from EmotionReport e where e.topic=:tpName")
    EmotionReport findByTopic(@Param("tp") String tpName);

    @Query("from EmotionReport e")
    List<EmotionReport> listReports();
}
