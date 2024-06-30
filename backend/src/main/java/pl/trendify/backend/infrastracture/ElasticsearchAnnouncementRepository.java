package pl.trendify.backend.infrastracture;

import co.elastic.clients.elasticsearch.ElasticsearchAsyncClient;
import co.elastic.clients.elasticsearch.core.IndexResponse;
import lombok.extern.slf4j.Slf4j;
import pl.trendify.backend.domain.ScraperDataDto;

import java.util.concurrent.CompletableFuture;

@Slf4j
public class ElasticsearchAnnouncementRepository implements  AnnouncementRepository{
    private final ElasticsearchAsyncClient esClient;

    public ElasticsearchAnnouncementRepository(ElasticsearchAsyncClient esClient) {
        this.esClient = esClient;
    }

    @Override
    public CompletableFuture<IndexResponse> addAnnouncement(ScraperDataDto dto) {
        log.info("addAnnouncement");

        return esClient.index(i -> i
                .index("otodom-announcements")
                .document(dto.data())
        ).exceptionally(e -> {
            log.error("Cannot addAnnouncement", e);
                return null;
    });

    }
}
