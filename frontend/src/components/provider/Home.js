import React, { useState } from 'react';

import { UserModel } from '../model';
import { HomeController } from '../view';
import { HomeViewModel } from '../viewmodel';


const Home = () => {
    const model = new UserModel();
    const [viewModel] = useState(new HomeViewModel(model));
    return (
        <HomeController viewModel={viewModel}/>
    ); 
};

export default Home;