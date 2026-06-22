# 전체 페이지 목록 집계
from . import main, areas, stations, lifezones, info, about

PAGES = (
    [main.PAGE]
    + areas.PAGES
    + stations.PAGES
    + lifezones.PAGES
    + info.PAGES
    + [about.PAGE]
)
