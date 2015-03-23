server {
        listen   80;
        server_name  app localhost;

        access_log  /var/log/nginx/app.access.log;

        root   /opt/app;
        index  index.html index.htm index.php;

	location / {
                proxy_pass                  http://127.0.0.1:10000/;
                proxy_redirect              off;
                proxy_set_header            Host            $host;
                proxy_set_header            X-Real-IP       $remote_addr;
                proxy_set_header            X-Forwarded-For  $proxy_add_x_forwarded_for;

                client_max_body_size        5M;
                client_body_buffer_size     5M;

                proxy_connect_timeout       30;
                proxy_send_timeout          30;
                proxy_read_timeout          30;

                proxy_buffer_size           16k;
                proxy_buffers               16 128k;
                proxy_busy_buffers_size     512k;
                proxy_temp_file_write_size  512k;
        }
}
