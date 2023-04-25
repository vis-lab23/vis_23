import { AutoIncrement, Column, Model, PrimaryKey, Table } from "sequelize-typescript";

@Table({
    timestamps: false
})
export class Category extends Model {
    @PrimaryKey
    @AutoIncrement
    @Column
    nummer?: number;

    @Column
    name: string;
}