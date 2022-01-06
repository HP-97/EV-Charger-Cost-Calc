export class Settings {
	API_HOST: string
	API_PORT: string
	FTP_HOST: string
	FTP_PORT: string
	FTP_USER: string
	FTP_PASS: string

	constructor() {
		this.API_HOST = process.env.API_HOST || '0.0.0.0';
		this.API_PORT = process.env.API_PORT || '3000';
		this.FTP_HOST = process.env.FTP_HOST
		this.FTP_PORT = process.env.FTP_PORT
		this.FTP_USER = process.env.FTP_USER
		this.FTP_PASS = process.env.FTP_PASS
	}
}