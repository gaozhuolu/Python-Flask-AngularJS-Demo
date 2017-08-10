var myApp = angular.module('myApp', ['ngRoute',
    'ngProgress',
    'angularUtils.directives.dirPagination',
    /*'chart.js',*/
    /*'ngCookies',*/
    'ngLoadingSpinner',
    'ngMaterial',
    /*'ngMessages',*/
    /*'ngImgCrop',
    'ngFileUpload', 'UserValidation'*/]);

myApp.config(['$locationProvider', function($locationProvider) {
    $locationProvider.hashPrefix('');
}]);

myApp.config(function($mdDateLocaleProvider) {
    $mdDateLocaleProvider.formatDate = function(date) {
        return moment(date).format('MM/DD/YYYY');
    };
});

myApp.config(function ($routeProvider) {
    $routeProvider
        //.when('/', {
        //    templateUrl: 'static/templates/login.html',
        //    controller: 'loginController',
        //    access: {restricted: false}
        //})
        //
        //.when('/login', {
        //    templateUrl: 'static/templates/login.html',
        //    controller: 'loginController',
        //    access: {restricted: false}
        //})
        .when('/', {
            templateUrl: 'static/templates/scrap.html',
            controller: 'scrapController',
            access: {restricted: false}
        })
        .otherwise({
            redirectTo: '/'
        });

        // use the HTML5 History API
        //$locationProvider.html5Mode(true);
});

//myApp.run(function ($rootScope, $location, $route, AuthService) {
//    $rootScope.$on('$routeChangeStart',
//        function (event, next, current) {
//            console.log('--------route Change Start --------');
//            console.log('event', event);
//            console.log('next', next.$$route);
//            console.log('current', current);
//            //console.log('restricted', next.access.restricted);
//            // console.log('isLoggedIn', AuthService.isLoggedIn());
//
//            if(typeof next.controller !== 'undefined') {
//                if(next.controller == 'loginController') {
//                    if (AuthService.isLoggedIn()) {
//                        $location.path('/dashboard');
//                        //$route.reload();
//                        return;
//                    }
//                }
//            }
//
//            if(typeof next.access === 'undefined') return;
//            //if(next.access.restricted && !AuthService.isLoggedIn()) {
//            //    $location.path('/login');
//            //    //$route.reload();
//            //    return;
//            //}
//
//
//            AuthService.getUserStatus()
//                .then(function(response){
//                    if(typeof next.controller !== 'undefined') {
//                        if(next.controller == 'loginController' && AuthService.isLoggedIn()) {
//                            $location.path('/dashboard');
//                            //$route.reload();
//                            return;
//                        }
//                    }
//                    console.log(AuthService.isLoggedIn());
//                    if (typeof next.access !== 'undefined' && next.access.restricted && !AuthService.isLoggedIn()){
//                        $location.path('/login');
//                        //$route.reload();
//                    }
//                });
//        }
//    );
//});