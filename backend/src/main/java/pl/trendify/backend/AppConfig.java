package pl.trendify.backend;

import co.elastic.clients.elasticsearch.ElasticsearchAsyncClient;
import lombok.extern.slf4j.Slf4j;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import pl.trendify.backend.infrastracture.ElasticSearchClient;
import pl.trendify.backend.infrastracture.ElasticsearchAnnouncementRepository;

@Configuration
@Slf4j
public class AppConfig {



    @Bean
    public ElasticsearchAsyncClient esClient() {
        // Configure and return the ElasticsearchClient
        log.info("elasticsearchClient");
        ElasticsearchAsyncClient esClient = new ElasticSearchClient().initClient();
        return esClient;
        //TODO is it good approach?
    }

    @Bean
    public ElasticsearchAnnouncementRepository announcementRepository(ElasticsearchAsyncClient esClient) {
        log.info("announcementRepository");
        return new ElasticsearchAnnouncementRepository(esClient);
    }

}
