FROM redmine
RUN sed -i -e "$ i RedmineApp::Application.routes.default_scope = \"/redmine\"" config/environment.rb && \
    echo "Redmine::Utils::relative_url_root = \"/redmine\"" >> config/environment.rb && \
    ln -sf ${PWD}/public ${PWD}/public/redmine
