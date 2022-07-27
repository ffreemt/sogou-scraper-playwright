"""Test."""
from about_time import about_time
from sogou_scraper_pw import sogou_tr
from logzero import logger
from icecream import ic


def test_sogou_tr1():
    """Test 1."""
    with about_time() as dur:
        res = sogou_tr("Test me")
    print(dur.duration_human)  # 67.5
    assert "测" in res or "我" in res
    logger.debug("dur1: %s", dur.duration_human)

    with about_time() as dur:
        res = sogou_tr("Test me 2\n\nTest me 3")
    print(res)
    logger.info("res: %s", res)
    ic(res)
    print(dur.duration_human)  # 25.4
    logger.debug("dur2: %s", dur.duration_human)

    assert "测" in res or "我" in res
