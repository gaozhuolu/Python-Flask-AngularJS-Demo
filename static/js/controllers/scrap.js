angular.module('myApp').controller('scrapController',
  ['$scope', '$http', '$routeParams', 'ngProgressFactory', '$location',
  function ($scope, $http, $routeParams, ngProgressFactory, $location) {
    //$scope.progressbar          = ngProgressFactory.createInstance();
    //$scope.addresslist          = null;
    ////page navigation.
    //$scope.currentPage = 1;
    //$scope.pageSize = 10;
    //
    ////default parameters
    //$scope.straddress = '100 S DOHENY DR'
    //$scope.strcity = 'Los Angeles'
    //$scope.strstate = 'CA'
    //$scope.strzip = '90048'
    //
    //
    //$scope.searchlist = function () {
    //  $scope.progressbar.reset();
    //  $scope.progressbar.start();
    //
    //  $http.post('/api/getaddresslist', {straddress:$scope.straddress, strcity:$scope.straddress, strstate:$scope.strstate, strzip:$scope.strzip})
    //      .then(function (response) {
    //        $scope.progressbar.complete();
    //        $scope.addresslist = response.data.list;
    //      },
    //      function (error) {
    //        $scope.progressbar.complete();
    //        console.log(error);
    //      }
    //  );
    //}
}]);