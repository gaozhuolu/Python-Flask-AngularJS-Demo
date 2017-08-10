angular.module('myApp').factory('AuthService',
  ['$q', '$timeout', '$http', '$rootScope',
  function ($q, $timeout, $http, $rootScope) {

    // create user variable
    var user = null;
    var meinfo = null;

    // return available functions for use in controllers
    return ({
      isLoggedIn: isLoggedIn,
      login: login,
      logout: logout,
      register: register,
      getUserStatus: getUserStatus
    });

    function isLoggedIn() {
      if(user) {
        $rootScope.meinfo = meinfo;
        //console.log('isLoggedIn');
        //console.log($rootScope.meinfo);
        return true;
      } else {
        $rootScope.meinfo = null;
        //console.log('isLoggedIn');
        //console.log($rootScope.meinfo);
        return false;
      }
    }

    function login(email, password) {
      // create a new instance of deferred
      var deferred = $q.defer();

      // send a post request to the server
      $http.post('/api/user/login', {useremail: email, userpassword: password})
        .then(
          function successCallback(response) {
            if(response.data.result){
              user = true;
              meinfo = response.data.meinfo;
              $rootScope.meinfo = meinfo;
              deferred.resolve();
              //console.log('login');
              //console.log($rootScope.meinfo);
            } else {
              user = false;
              meinfo = null;
              $rootScope.meinfo = null;
              deferred.reject();
              //console.log('login');
              //console.log($rootScope.meinfo);
            }
          },

          function errorCallback(response) {
            user = false;
            meinfo = null;
            $rootScope.meinfo = null;
            deferred.reject();
            //console.log('login');
            //console.log($rootScope.meinfo);
          }
      );

      // return promise object
      return deferred.promise;

    }

    function logout() {
      // create a new instance of deferred
      var deferred = $q.defer();

      // send a post request to the server
      $http.post('/api/user/logout', {})
        .then(
          function successCallback(response) {
            user = false;
            meinfo = null;
            $rootScope.meinfo = null;
            deferred.resolve();
          },

          function errorCallback(response) {
            user = false;
            meinfo = null;
            $rootScope.meinfo = null;
            deferred.reject();
          }
      );

      // return promise object
      return deferred.promise;
    }

    function register(username, useremail, userpassword) {
      // create a new instance of deferred
      var deferred = $q.defer();

      // send a post request to the server
      $http.post('/api/user/register', {username: username, useremail: useremail, userpassword: userpassword})
        .then(function (response) {
          if(response.data.result){
            deferred.resolve();
          } else {
            deferred.reject();
          }
        },
        function (response) {
          deferred.reject();
        });

      // return promise object
      return deferred.promise;
    }

    function getUserStatus() {
      return $http.post('/api/user/status', {})
        .then(
          function successCallback(response) {
            if(response.data.status){
              user = true;
              meinfo = response.data.meinfo;
              $rootScope.meinfo = meinfo;
              //console.log('getUserStatus');
              //console.log($rootScope.meinfo);
            }
            else {
              user = false;
              meinfo = null;
              $rootScope.meinfo = null;
              //console.log('getUserStatus');
              //console.log($rootScope.meinfo);
            }
          },

          function errorCallback(response) {
            user = false;
            meinfo = null;
            $rootScope.meinfo = null;
          }
      );
    }

}]);