import React from 'react';
import { HashRouter as Router, Route, Switch } from 'react-router-dom';
import HouseProfile from 'routes/HouseProfile';
import Houses from 'routes/Houses';
import Profile from 'routes/Profile';
import Auth from 'routes/Auth';
import Main from 'routes/Main';

const AppRouter = ({ isLoggedIn }) => {
  return (
    <Router>
      <Switch>
        {isLoggedIn ? (
          <>
            <Route exact path="/" component={Main} />
          </>
        ) : (
          <Route exact path="/" component={Auth} />
        )}

        <Route path="/">
          <Profile />
        </Route>

        <Route path="/">
          <Houses />
        </Route>

        <Route path="/">
          <HouseProfile />
        </Route>
      </Switch>
    </Router>
  );
};

export default AppRouter;
