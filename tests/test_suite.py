from tests import fix_client, fix_suite  # import is used


def test_response_to_dict():
    from adobe_analytics.suite import Suite
    response = [{
        "id": "pageviews",
        "name": "Page Views"
    }, {
        "id": "evar1",
        "name": "visit intend"
    }]
    result = Suite._response_to_dict(response)

    expected_result = {
        "pageviews": {
            "id": "pageviews",
            "name": "Page Views"
        },
        "evar1": {
            "id": "evar1",
            "name": "visit intend"
        }
    }
    assert result == expected_result


def test_metrics_is_dict(fix_suite):
    assert isinstance(fix_suite.metrics(), dict)


def test_elements_is_dict(fix_suite):
    assert isinstance(fix_suite.dimensions(), dict)


def test_segments_is_dict(fix_suite):
    assert isinstance(fix_suite.segments(), dict)
