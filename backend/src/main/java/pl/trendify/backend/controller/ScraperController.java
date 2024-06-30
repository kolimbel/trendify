package pl.trendify.backend.controller;

import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import pl.trendify.backend.domain.ScraperDataDto;
import pl.trendify.backend.service.AnnouncementProcessingService;

import java.util.Map;

@RestController
@RequestMapping("/api/v1/scraper")
@Slf4j
public class ScraperController {
    @Autowired
    private AnnouncementProcessingService scraperService;

    @PostMapping("/data")
    public ResponseEntity<String> receiveData(@RequestBody Map<String, Object> data) {
        log.info(data.toString());
        ScraperDataDto dto = new ScraperDataDto(data);
        scraperService.processScraperData(dto);
        return ResponseEntity.ok("Data received");
    }

    @PostMapping("/data-test")
    public ResponseEntity<String> receiveDataTest(@RequestBody Map<String, Object> data) {
        log.info(data.toString());
        return ResponseEntity.ok("Data received");
    }
}
