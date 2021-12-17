package com.example.emotionanalysis;

import com.example.emotionanalysis.interceptor.AdminInterceptor;
import com.example.emotionanalysis.interceptor.UserInterceptor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.InterceptorRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

@Configuration
public class WebMvcConfig implements WebMvcConfigurer {
    @Autowired
    private AdminInterceptor adminIntercepter;
    @Autowired
    private UserInterceptor userInterceptor;
    public void addInterceptor(InterceptorRegistry registry){
        registry.addInterceptor(adminIntercepter)
                .addPathPatterns("api/admin/**");
        registry.addInterceptor(userInterceptor)
                .addPathPatterns("api/user/**");

    }
}
