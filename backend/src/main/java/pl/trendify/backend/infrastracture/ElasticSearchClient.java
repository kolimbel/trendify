package pl.trendify.backend.infrastracture;

import co.elastic.clients.elasticsearch.ElasticsearchAsyncClient;
import co.elastic.clients.json.jackson.JacksonJsonpMapper;
import co.elastic.clients.transport.ElasticsearchTransport;
import co.elastic.clients.transport.rest_client.RestClientTransport;
import org.apache.http.HttpHost;
import org.elasticsearch.client.RestClient;

public class ElasticSearchClient {
    // URL and API key
    private final String serverUrl = "http://localhost:9200";

    /**
     * Creates the low-level client
     *
     * @return
     */

    private RestClient initRestClient() {
        return RestClient
                .builder(HttpHost.create(serverUrl))
                .build();
    }

    /**
     * Creates the transport with a Jackson mapper
     *
     * @return
     */
    private ElasticsearchTransport initTransport(RestClient restClient) {
        return new RestClientTransport(
                restClient, new JacksonJsonpMapper());
    }

    public ElasticsearchAsyncClient initClient() {
        RestClient restClient = initRestClient();
        ElasticsearchTransport transport = initTransport(restClient);
        return new ElasticsearchAsyncClient(transport);
    }


}
