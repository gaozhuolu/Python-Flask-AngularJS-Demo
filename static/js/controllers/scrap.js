angular.module('myApp').controller('scrapController',
  ['$scope', '$http', '$routeParams', 'ngProgressFactory', '$location',
  function ($scope, $http, $routeParams, ngProgressFactory, $location) {
    $scope.progressbar          = ngProgressFactory.createInstance();
    $scope.searchlist           = null;
    //page navigation.
    $scope.currentPage = 1;
    $scope.pageSize = 10;
    $scope.tab = 'web';
    $scope.searchkey = '';

    $scope.changedTab      = function(value) {
      $scope.tab = value;
    };

    $scope.doYandexSearch = function () {
      $scope.progressbar.reset();
      $scope.progressbar.start();

      $http.post('/api/yandex/search', {key:$scope.searchkey, tab:$scope.tab})
          .then(function (response) {
            console.log(response.data);
            if(response.data.status) {
              $scope.searchlist = response.data.results;
            }
            else {
              $scope.searchlist = null;
              console.log(response.data.errmsg);
            }
            $scope.progressbar.complete();
          },
          function (error) {
            $scope.progressbar.complete();
            console.log(error);
          }
      );
    }
}]);
