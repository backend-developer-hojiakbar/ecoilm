from .views import (
    homePages,
    aboutPage,
    newsPages,
    activityPages,
    connectPages,
    openBudgetPages,
    scienceJournal,
    newsDetail,
    firstProjectsList,
    secondProjectsList,
    projectDetail1,
    projectDetail2,
    projectDetail3,
    projectDetail4,
    projectDetail5,
    projectDetail6,
    projectDetail7,
    projectDetail8,
    projectDetail9,
    projectDetail10,
    projectDetail,
    redBook,
    commingSoon,
    labar,
    tuzilma,
    rahbariyat_list,
    qonunlarList,
    vazifa_funksiyalar,
    send_article,
    ilmiyKengash,
    patentlar,
    moddalar,
    books,
xamkor
)

from django.urls import path

urlpatterns = [
    path('', homePages, name="home-page"),
    path('about/', aboutPage, name="aboutPages"),
    path('news/', newsPages, name="news-pages"),
    path('activity/', activityPages, name="activity-pages"),
    path('connect/', connectPages, name="connect-pages"),
    path('science-journal/', scienceJournal, name="science-pages"),
    path('red-book/', redBook, name="qizil-kitob"),
    path('open-budget/', openBudgetPages, name="openBudget-pages"),
    path('news-detail/<int:id>', newsDetail, name="news-detail"),
    path('fist-projects/', firstProjectsList, name="first-projects"),
    path('second-projects/', secondProjectsList, name="second-projects"),
    path('project-detail/', projectDetail, name="project-detail"),
    path('project-detail-1/', projectDetail1, name="project-detail-1"),
    path('project-detail-2/', projectDetail2, name="project-detail-2"),
    path('project-detail-3/', projectDetail3, name="project-detail-3"),
    path('project-detail-4/', projectDetail4, name="project-detail-4"),
    path('project-detail-5/', projectDetail5, name="project-detail-5"),
    path('project-detail-6/', projectDetail6, name="project-detail-6"),
    path('project-detail-7/', projectDetail7, name="project-detail-7"),
    path('project-detail-8/', projectDetail8, name="project-detail-8"),
    path('project-detail-9/', projectDetail9, name="project-detail-9"),
    path('project-detail-10/', projectDetail10, name="project-detail-10"),
    path('comming-soon/', commingSoon, name="comming_soon"),
    path('labar/', labar, name="labar_name"),
    path('tuzilma/', tuzilma, name="tuzilma"),
    path('rahbariyat-list/', rahbariyat_list, name="rahbariyat_list_page"),
    path('qonunlar-list/', qonunlarList, name="qonunlar_list"),
    path('vazifa-funksiyalar/', vazifa_funksiyalar, name="vazifa_funksiyalar"),
    path('send-article/', send_article, name="send_article"),
    path('patentlar/', patentlar, name="patentlar"),
    path('moddalar', moddalar, name="moddalar"),
    path('book', books, name="books"),
    path('xamkor', xamkor, name="xamkor"),
    path('ilmiy-kengash/', ilmiyKengash, name="ilmiy_kengash")

    
]














