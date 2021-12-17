package com.example.emotionanalysis.enums;


import org.springframework.beans.factory.annotation.Value;

import java.util.Arrays;

/**
 * 对于用户权限类型的枚举
 */
public enum RoleEnums {
    USER(1, "用户"),
    ADMINISTRATOR(2, "管理员");


    private Integer code;

    private String message;

    RoleEnums(Integer code, String message) {
        this.code = code;
        this.message = message;
    }
}
