def test_builder_uploading(main_page, stage_builder_page, logout_after_test):
    main_page = main_page()
    login_page = main_page.click_build_for_free_button(is_user_logged_in=False)
    login_page.login()
    builder_page = stage_builder_page(is_open=False)
    builder_page.confirm_limited_tablet_alert().wait_for_loading_screen().wait_for_loading_screen_to_be_finished()
    builder_page.close_onboarding_alert()
