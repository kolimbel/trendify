package pl.trendify.backend.infrastracture;

import co.elastic.clients.elasticsearch.core.IndexResponse;
import pl.trendify.backend.domain.ScraperDataDto;

import java.util.concurrent.CompletableFuture;

public interface AnnouncementRepository {

    CompletableFuture<IndexResponse> addAnnouncement(ScraperDataDto dto);
}
