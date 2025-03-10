package com.example.demo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@SpringBootApplication
public class DemoApplication {

	public static void main(String[] args) {
		SpringApplication.run(DemoApplication.class, args);
	}

}

@RestController
class HelloController {
    
    @GetMapping("/")
    public String hello() {
        return "Hello from containerized Spring Boot application!";
    }
    
    @GetMapping("/info")
    public String info() {
        return "Java version: " + System.getProperty("java.version") +
               ", Available processors: " + Runtime.getRuntime().availableProcessors();
    }
}