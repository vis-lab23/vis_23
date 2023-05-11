import { HttpService } from '@nestjs/axios';
import { HttpException, Injectable, Logger } from '@nestjs/common';
import fetch from 'node-fetch';

@Injectable()
export class ProductClientService {
    constructor(private readonly httpService: HttpService) {}
    private readonly logger = new Logger(ProductClientService.name);

    async deleteByCategoryId(id: number) {
        try {
            await fetch(`${process.env.PRODUCT_SERVICE_ADRESS}/${id}/`, { method: 'DELETE' });
            this.logger.log(`Deleted all products with Category number ${id}`);
        } catch (err) {
            this.logger.error("An error occured while deleting Products of Category " + id);
            throw new HttpException('Delete failed: Could not delete Corresponding Products.', 500);
        }
    }
}
