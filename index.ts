import express, {Request, Response, Router} from 'express';
import { Settings } from './core/config';
const app = express();
const routerV1 = Router();
const settings = new Settings();

routerV1.get('/', (req: Request, res: Response) => {
	const resp = {"hello": "world"};
	res.send(resp);
});

routerV1

app.use('/v1', routerV1);

app.listen(settings.API_PORT, () => {
	console.log(`App listening to http://localhost:${settings.API_PORT}`)
});