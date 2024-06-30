package pl.trendify.backend.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import pl.trendify.backend.domain.ScraperDataDto;
import pl.trendify.backend.infrastracture.AnnouncementRepository;


@Service
public class AnnouncementProcessingService {
    //queueService
    //ann repository

    @Autowired
    AnnouncementRepository announcementRepository;

    public void processScraperData(ScraperDataDto dto) {
        announcementRepository.addAnnouncement(dto);
    }
}
