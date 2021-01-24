import Login from '../pages/login.vue';
import UserHome from '../pages/userHome.vue';
import AdminHome from '../pages/adminHome.vue';
import UserRegistration from '../pages/userReg.vue';
import UserProfile from '../pages/userProfile.vue';
import AdminRegistration from '../pages/adminReg.vue';
import UpdateShots from '../pages/updateShots.vue';
import NotFoundPage from '../pages/404.vue';

var routes = [
  {
    path: '/',
    component: Login,
  },
  {
    path: '/login/',
    component: Login,
  },
  {
    path: '/userReg/',
    component: UserRegistration,
  },
  {
    path: '/adminReg/',
    component: AdminRegistration,
  },
  {
    path: '/userHome/',
    component: UserHome,
  },
  {
    path: '/userProfile/',
    component: UserProfile,
  },
  {
    path: '/adminHome/',
    component: AdminHome,
  },
  {
    path: '/updateShots/',
    component: UpdateShots,
  },
  {
    path: '(.*)',
    component: NotFoundPage,
  },
];

export default routes;
